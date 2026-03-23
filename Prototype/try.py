import torch
import paddle


print(paddle.device.get_device())
print(torch.cuda.is_available())