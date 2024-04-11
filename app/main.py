import uvicorn
from fastapi import FastAPI


app = FastAPI()

from app.routes.task_1 import router as r_1
app.include_router(r_1)

from app.routes.task_2 import router as r_2
app.include_router(r_2)

from app.routes.task_3 import router as r_3
app.include_router(r_3)

from app.routes.task_4 import router as r_4
app.include_router(r_4)

from app.routes.task_5 import router as r_5
app.include_router(r_5)

from app.routes.task_6 import router as r_6
app.include_router(r_6)

# from app.routes.task_7 import router as r_7
# app.include_router(r_7)
#
# from app.routes.task_8 import router as r_8
# app.include_router(r_8)
#
# from app.routes.task_11 import router as r_11
# app.include_router(r_11)

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)
