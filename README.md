# docker-collaboration

# Contributors 
    Kelompok 3
    - Anak Agung Ngurah Bagus Rama Putra Suteja - 2802531460
    - Brian Filbert Chandra - 2802529733
    - Digyo Rizky Shine Brutu - 2802523244
    - Seraphine Kartolo - 2802526100
    - Muhammad Rafi Bagaskara - 2802510185

# Description
This is a docker collaboration project consisting a SSTI debug web to learn basic web exploitation.

# Using docker step by step
Download the code from GitHub:
```bash
git clone https://github.com/Cipaimian/web-exploitation-script.git
```
Move to one of the script directory:
```bash
cd web-exploitation-script/ssti-debug
```
Check for file ```Dockerfile``` inside the directory
```bash
$ ls
app.py  Dockerfile  requirements.txt
```
Build the image using docker command:
```bash
docker build -t project-name .

-t project-name = image name
.               = image will be made inside current directory
```
Run the container:
```bash
docker run -it --rm -p 10000:10000 project-name
```
```
-it             = better interaction for terminal
--rm            = automatically deletes the container when it stops
-p 10000:10000  = stands for port, host_port:container_port
```
The app is running in browser:
```bash
http://127.0.0.1:10000
```