# 类比：dataclass 是“自动写__init__的傻瓜模式”
# Pydantic 是“dataclass + 在运行时检查类型 + 自动转换 + 错误信息漂亮”

from pydantic import BaseModel, EmailStr, Field, field_validator


# 创建对象时自动校验元素是否合规，并且有校验器对 name 做进一步校验
class User(BaseModel):              # 这样就像有了 dataclass
    id: int
    name: str = Field(min_length=1, max_length=20)    # Field 会约束字段范围
    age: int = Field(ge=0, le=150)          # ge是大于等于， le是小于等于
    email: EmailStr             # 校验邮箱格式
    tags: list[str] = []

    @field_validator("name")    # 自定义字段校验器
    @classmethod
    def name_no_space(cls, v: str) -> str:
        if " " in v:
            raise ValueError("name 不能含空格")
        return v.strip()

# str 自动转 int
# u = User(id="1", name="Alice", age=18, email="123@qq.com")          # 这里 mypy 会报错，但是会自动转换
u = User(id=1, name="Alice", age=18, email="123@qq.com")
print(u)

# 校验失败
try:
    User(id=2, name="A B", age=-1, email="not-an-email")
except Exception as e:
    print(e)
"""
这是 id 是 "x" 的输出
4 validation errors for User
id
  Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='x', input_type=str]
name
  Value error, name 不能含空格 [type=value_error, input_value='A B', input_type=str]
age
  Input should be greater than or equal to 0 [type=greater_than_equal, input_value=-1, input_type=int]
email
  value is not a valid email address: An email address must have an @-sign. [type=value_error, input_value='not-an-email', input_type=str]
"""

# 序列化：model_dump / model_dump_json
print(u.model_dump())               # 转为字典
print(u.model_dump_json())          # 转为 JSON

# 反序列化
data = {"id": 2, "name": "Bob", "age": 30, "email": "456@qq.com"}
u2 = User.model_validate(data)      # 注意这里还会加上 tags 这个属性
print(u2)