from fastapi import APIRouter
from app.database import members_collection
from app.models import Member

router = APIRouter(prefix="/members", tags=["Members"])

@router.post("/")
def add_member(member: Member):
    result = members_collection.insert_one(member.model_dump())
    return {"id": str(result.inserted_id)}

@router.get("/")
def get_members():
    members = []
    for m in members_collection.find():
        m["_id"] = str(m["_id"])
        members.append(m)
    return members