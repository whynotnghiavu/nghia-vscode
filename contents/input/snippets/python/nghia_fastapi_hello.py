@hello_router.get(
    # post, put, delete, ...
    '/hello',
    description="Mô tả Hello",
    # response_model=Response
    # response_model=Response
    # response_model=Response
    # dependencies=[Security(AuthHandler().scope_and_user_with_check_otp("admin", "analyst"))],
)
async def ten_ham_hello(
    # Phân trang limit, offset, ... có toltal
    # Phân trang from, size, ... có toltal
    # request Body
    # request Body
    # request Body
):
    # )-> Response:
    # )-> Response:
    # )-> Response:

    # Tạo docs cuối cùng
    # Tạo docs cuối cùng
    # Tạo docs cuối cùng

    logger.info(f'Mô tả Hello')
    return await {'message': 'Hello World'}
