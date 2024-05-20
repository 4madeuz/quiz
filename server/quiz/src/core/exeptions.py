from fastapi import HTTPException, status


class ModelNotFoundException(HTTPException):
    def __init__(self) -> None:
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='Object does not found',
        )


class InvalidFieldException(HTTPException):
    def __init__(self) -> None:
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Invalid value',
        )
