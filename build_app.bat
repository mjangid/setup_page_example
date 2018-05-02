SET PATH="C:\Program Files\7-Zip\";%PATH%
7z a -ttar setup_page_example setup_page_example
7z a -tgzip setup_page_example.spl setup_page_example.tar
DEL /Q setup_page_example.tar