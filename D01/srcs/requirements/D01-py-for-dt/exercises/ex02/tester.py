from load_image import ft_load

GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

try:
    print(f"{GREEN}TEST 01 - Open .jpg file:{RESET}")
    print(ft_load("imgs/landscape.jpg"))
except Exception as e:
    print(f"{type(e).__name__}: {e}")

try:
    print(f"{GREEN}TEST 02 - Open .jpeg file:{RESET}")
    print(ft_load("imgs/animal.jpeg"))
except Exception as e:
    print(f"{type(e).__name__}: {e}")

try:
    print(f"{RED}TEST 03 - Path is not of string type:{RESET}")
    print(ft_load(42))
except Exception as e:
    print(f"{type(e).__name__}: {e}")

try:
    print(f"{RED}TEST 04 - Image is not of .jpg or .jpeg type:{RESET}")
    print(ft_load("landscape.png"))
except Exception as e:
    print(f"{type(e).__name__}: {e}")

try:
    print(f"{RED}TEST 05 - Image does not exist:{RESET}")
    print(ft_load("imgs/landscape.JPEG"))
except Exception as e:
    print(f"{type(e).__name__}: {e}")
