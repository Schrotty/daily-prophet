import multiprocessing

bind = "0.0.0.0:8080"
daemon = False
timeout = 0
chdir = '..'
workers = multiprocessing.cpu_count() * 2 + 1
