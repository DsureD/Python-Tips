from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware


# 创建 FastAPI 实例
app = FastAPI(title="FastAPI 示例")

# 允许跨域的配置
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 允许所有域名访问（生产环境请改为具体域名）
    allow_credentials=True,
    allow_methods=["*"],  # 允许所有请求方法
    allow_headers=["*"],  # 允许所有请求头
)


# GET 请求示例
@app.get("/hello")
def get_rq(name: str = "World"):
    return {"message": f"Hello, {name}!"}

# POST 请求示例
@app.post("/echo")
async def post_rq(request: Request):
    data = await request.json()
    return {"you_sent": data}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
