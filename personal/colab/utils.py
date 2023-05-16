from transformers import BertTokenizer
from transformers import BertForQuestionAnswering
import pandas as pd
import numpy as np
import torch
import os
module_dir = os.path.dirname(__file__)
file_path = os.path.join(module_dir, 'context.txt')  # full path to text.
data_file = open(file_path, 'r', encoding="utf8")
context = data_file.read()

model = BertForQuestionAnswering.from_pretrained(
    'bert-large-uncased-whole-word-masking-finetuned-squad')
tokenizer = BertTokenizer.from_pretrained(
    'bert-large-uncased-whole-word-masking-finetuned-squad')


def runQuery(input):
    inputs = tokenizer.encode_plus(
        input, context, return_tensors='pt', padding=True, truncation=True)
    outputs = model(**inputs)

    answer_start = torch.argmax(outputs[0])
    answer_end = torch.argmax(outputs[1]) + 1

    answer = tokenizer.convert_tokens_to_string(tokenizer.convert_ids_to_tokens(
        inputs['input_ids'][0][answer_start:answer_end]))
    if answer.startswith('[CLS]'):
        answer = "I am sorry, Unable to answer!"

    return answer
