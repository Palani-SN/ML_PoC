import os
import psutil

# Logical cores (including hyper-threading)
logical_cores = os.cpu_count()

# Physical cores
physical_cores = psutil.cpu_count(logical=False)

print(f"Logical cores: {logical_cores}")
print(f"Physical cores: {physical_cores}")
