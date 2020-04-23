import json
import re

p_sp=re.compile('\s+')
p_num=re.compile('\d+')

f='text.txt'

reader=open(f)
vocabset={'PAD':0,'EOS':1,'SEP':2,'UNK1':3,'UNK2':4,'UNK3':5}
writer=open('corpus.txt','w')

for line in reader.readlines():
    line=line.strip()
    if line:
        line=p_sp.sub('',line)
        line=p_num.sub('m',line)
        for w in line:
            if w not in vocabset:
                vocabset[w]=len(vocabset)

        line=' '.join(list(line)+['EOS'])
        writer.write(line+'\n')


#####
print (len(vocabset))
writer=open('vocab.json','w')
writer.write(json.dumps(vocabset,ensure_ascii=False))


########
config = {
	"architectures": [
		"GPT-2"
	],
	"attention_probs_dropout_prob": 0.1,
	"hidden_act": "gelu",
	"hidden_dropout_prob": 0.1,
	"hidden_size": 768,
	"initializer_range": 0.02,
	"intermediate_size": 3072,
	"layer_norm_eps": 1e-05,
	"max_position_embeddings": 514,
	"model_type": "gpt-2",
	"num_attention_heads": 12,
	"num_hidden_layers": 4,
	"type_vocab_size": 1,
	"vocab_size": 52000
}
with open("./config.json", 'w') as fp:
    fp.write(json.dumps(config,indent=4))

tokenizer_config = {
	"max_len": 1024
}
with open("./tokenizer_config.json", 'w') as fp:
    fp.write(json.dumps(tokenizer_config,indent=4))