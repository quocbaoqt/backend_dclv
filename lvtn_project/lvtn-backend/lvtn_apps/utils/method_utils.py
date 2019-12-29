import random, string, uuid
import os


def generate_sequence(N):
    return ''.join(random.SystemRandom().choice(string.ascii_uppercase + 
    string.ascii_lowercase + string.digits + '@_') for _ in range(N))


def generate_name_image(instance, filename):
    path = instance.__class__.__name__
    name = filename[:filename.rfind('.')]
    ext = filename[filename.rfind('.'):]
    filename = '{}_{}{}'.format(name, generate_sequence(8), ext)
    final_name = os.path.join(path, filename)
    return final_name