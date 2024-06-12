

# from pathlib import Path

# file_path="D:\\vidhi_project\\demo.html\\check.html"

# with open(file_path,"rb") as file:
#     content = file.read()
# save_path=Path.home().joinpath("Downloads",Path(file_path).name)

# save_path.write_bytes(content)
# print(f"file save to {save_path}")


from pathlib import Path                    

file_path = Path("D:\\vidhi_project\\demo.html\\books.html")
save_path = Path.home() / "Downloads" / file_path.name

save_path.write_bytes(file_path.read_bytes())
print(f"File saved to {save_path}")


