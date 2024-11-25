class Request_Response(BaseModel):
    interval: int = Field(
        1,
        description="The interval of the schedule",
    )
