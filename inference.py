from tokenizers import Tokenizer
import torch
from pages.model.model import Seq2SeqTransformer, config
import argparse

tokenizer = Tokenizer.from_file('tokenizer.json')

special_tokens = {
    '<unk>': 0,
    '<pad>': 1,
    '<s-en>': 2, # bos english
    '<s-te>': 3, # bos telugu
    '</s>': 4, # eos
}


model = Seq2SeqTransformer(config)

state_dict = torch.load('best_model.pt',map_location='cpu')
model.load_state_dict(state_dict)

def translate(input_sentence,language='hi',d=True,t=1.0):
    input_ids = f"<s-en>{input_sentence.strip()}</s>"
    input_ids = tokenizer.encode(input_ids).ids
    input_ids = torch.tensor(input_ids,dtype=torch.long).unsqueeze(0)
    bos = special_tokens[f"<s-{language}>"]
    outputs = model.generate(input_ids,deterministic=d,bos=bos,temperature=t)
    translation = tokenizer.decode(outputs.numpy())
    return translation

parser = argparse.ArgumentParser()
parser.add_argument('-l',default='te',required=True,help="te:telugu")
parser.add_argument('--text',required=True,help="english text to translate")
parser.add_argument('-s',default=True,action='store_true',help='do_sample')
parser.add_argument('-t',default=1.0,type=float,help='temperature')

args = parser.parse_args()

print(translate(input_sentence=args.text,language=args.l,d=not args.s,t=args.t))