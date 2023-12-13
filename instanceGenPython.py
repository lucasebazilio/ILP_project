import os
import random


def generate_instance(file_path, nOrders, nSlots, p, l, c, mindi, maxdi, maxsur):
    with open(file_path, 'w') as file:
        file.write(f'[Values]\n')
        file.write(f'nOrders={nOrders}\n')
        file.write(f'nSlots={nSlots}\n')
        file.write(f'p={p}\n')
        file.write(f'l={l}\n')
        file.write(f'c={c}\n')
        file.write(f'mindi={mindi}\n')
        file.write(f'maxdi={maxdi}\n')
        file.write(f'maxsur={maxsur}\n')


def compute_values(nOrders, nSlots, id):
    p = [random.uniform(0, 200) for _ in range(nOrders)]
    l = [random.randint(1, nSlots) for _ in range(nOrders)]
    # maxsur = random.uniform(10.0, 80.0)
    maxsur = 50.0
    c = [random.uniform(1.0, maxsur) for _ in range(nOrders)]
    mindi = [random.randint(l[i], nSlots) for i in range(nOrders)]
    maxdi = [random.randint(mindi[i], nSlots) for i in range(nOrders)]

    instances_folder = 'instances'
    if not os.path.exists(instances_folder):
        os.makedirs(instances_folder)

    file_name = f'tunin_n{nOrders}_i{id}.dat'
    file_path = os.path.join(instances_folder, file_name)

    generate_instance(file_path, nOrders, nSlots, p, l, c, mindi, maxdi, maxsur)


def generate_massive(N):
    for i in range(1, N+1):
        compute_values(5000, 12, i)


if __name__ == "__main__":
    generate_massive(100)
