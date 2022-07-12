from minio import Minio
from minio.error import S3Error


def main():
    # Create a client with the MinIO server playground, its access key
    # and secret key.
    client = Minio(
        endpoint="localhost:9000",
        secure=False,
        access_key="093DrIkcXK8J3SC1",
        secret_key="CfjqeNxAtDLnUK8Fbhka8RwzfZTNlrf5",
    )

    # Make 'asiatrip' bucket if not exist.
    found = client.bucket_exists("asiatrip")
    if not found:
        client.make_bucket("asiatrip")
    else:
        print("Bucket 'asiatrip' already exists")



if __name__ == "__main__":
    try:
        main()
    except S3Error as exc:
        print("error occurred.", exc)
