import datetime
import os
import json

if __name__ == '__main__':
    print("Input your code here, end with \"///\" or Ctrl+D:")
    code = ""
    while True:
        try:
            line = input()
            if line == "///":
                break
            code += line + "\n"
        except EOFError:
            break
    language = 0 # 0 for python, 1 for c++
    if "#include" in code:
        language = 1
    elif "import" in code:
        language = 0
    else:
        language = input("Please input the language of your code (0 for python, 1 for c++): ")

    # save file to ./code/code_{time}
    if language == 0:
        filename = "code_" + datetime.datetime.now().strftime("%Y%m%d%H%M%S") + ".py"
    else:
        filename = "code_" + datetime.datetime.now().strftime("%Y%m%d%H%M%S") + ".cpp"
    with open(os.path.join("code", filename), "w") as f:
        f.write(code)
    print(f"Code saved to {filename}")

    # load json
    with open("config.json", "r") as f:
        config = json.load(f)

    # run the code
    if language == 0:
        pythonpath = config["python"]["python_path"]
        if pythonpath == "" or pythonpath == "YOUR_PYTHON_PATH":
            pythonpath = "python"
        argument = config["python"]["argument"]
        print(f"{filename} is running...")
        os.system(f"{pythonpath} {os.path.join('code', filename)} {argument}")
    else:
        gpppath = config["cpp"]["gpp_path"]
        if gpppath == "" or gpppath == "YOUR_g++_PATH":
            gpppath = "g++"
        argument = config["cpp"]["argument"]
        os.system(f"{gpppath} {os.path.join('code', filename)} -o {os.path.join('code', filename.split('.')[0])} {argument}")
        print(f"{filename} is running...")
        os.system(os.path.join('code', filename.split('.')[0]))