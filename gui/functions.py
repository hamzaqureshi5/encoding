#
# from pydantic import BaseModel
# from pydantic import BaseModel, Field, conint, constr
#
#
# class ICCID(BaseModel):
#     iccid: constr(min_length=18, max_length=20)  # type: ignore
#
#
# class IMSI(BaseModel):
#     imsi: constr(min_length=15, max_length=15)  # type: ignore
#
#
# class KEYS(BaseModel):
#     K4: constr(min_length=32, max_length=64)  # type: ignore
#     op: constr(min_length=32, max_length=32)  # type: ignore
#     ki: constr(min_length=32, max_length=32)  # type: ignore
