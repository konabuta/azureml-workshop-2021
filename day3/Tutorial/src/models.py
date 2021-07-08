import torch
from torch.nn.utils.rnn import pad_sequence
import pytorch_lightning as pl 
from transformers import BertModel

device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")


class BertClassification(torch.nn.Module):
    def __init__(self):
        super(BertClassification, self).__init__()
        self.bert = BertModel.from_pretrained('cl-tohoku/bert-base-japanese-whole-word-masking')
        self.dropout = torch.nn.Dropout(0.2)
        self.cls = torch.nn.Linear(768, 9)

    def forward(self, ids, attention_mask):
        _, output = self.bert(input_ids=ids, attention_mask=attention_mask, return_dict=False)
        output = self.dropout(output)
        output = self.cls(output)
        return output

class LitBert(pl.LightningModule):
    def __init__(self):
        super().__init__()
        self.bert = BertClassification().to(device)
    
    def forward(self, ids, attention_mask):
        output = self.bert(ids, attention_mask)
        return output

    def training_step(self, batch, batch_idx):
        ids = batch['input_ids']
        attention_mask = batch['attention_mask']
        output = self.bert(ids, attention_mask)
        ys = batch['targets']
        loss = torch.nn.CrossEntropyLoss()(output, ys)
        return loss
        
    def configure_optimizers(self):
        optimizer = torch.optim.SGD(self.bert.parameters(), lr=0.01)
        return optimizer