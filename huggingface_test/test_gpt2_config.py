from transformers import GPT2Model, GPT2Config,AutoConfig
# Initializing a GPT2 configuration
configuration = GPT2Config()

# Initializing a model from the configuration
model = GPT2Model(configuration)


config = AutoConfig.from_pretrained('./未命名文件夹/gpt2-medium-config.json')

print ('')