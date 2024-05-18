import io
import json

# from minio import Minio
import pandas as pd

# minio_client = Minio(
#     endpoint=MINIO_ENDPOINT,
#     access_key=MINIO_ACCESS_KEY,
#     secret_key=MINIO_SECRET_KEY,
#     secure=True,
# )
try:
    file_length = len(file_content)
except:
    file_length = -1

# Чтение списка объектов
bucket_name = "datahub-dbt-files"
directory = "oil"
filename_prefix = ""
collection = minio_client.list_objects(
    bucket_name=bucket_name, prefix=f"{directory}/{filename_prefix}"
)
for el in collection:
    print(el.object_name)

# Чтение объекта в датафрейм
obj = "filename.csv"
try:
    response = minio_client.get_object(
        bucket_name=bucket_name, object_name=f"{directory}/{obj}"
    )
    df = pd.read_csv(
        io.BytesIO(response.read()),
        parse_dates=["ts_start", "ts_end"],
    )
finally:
    response.close()
    response.release_conn()

# Чтение объекта в yaml
obj = "params/model_params.yml"
response = minio_client.get_object(
    bucket_name=bucket_name, object_name=f"{directory}/{obj}"
)
if response.status == 200:
    params_str = response.data.decode()
    params_dict = json.loads(params)

# Удаление объекта
minio_client.remove_object(
    object_name=f"{directory}/<filename>", bucket_name=bucket_name
)

# Запись объекта
minio_client.put_object(
    bucket_name,
    object_name,
    io.BytesIO(file_content),
    file_length,
    content_type=content_type,
)
