src_path = "/home/pubsrv/data/guorui/data"
# src_path = "/home/guorui/data"
data_path = src_path + "/Fold/0"
save_path = src_path + "/Res/Fold3/0"
num_GPU = 1
# src_path = "E:\Data\EmojiPrediction"
# data_path = src_path + "\Fold_head\/0"#src_path + "\Fold\/0"
# save_path = src_path + "\Res\Fold_head\/0"#src_path + "\Res\Fold\/0"
# num_GPU = 0

model = "small"
rnn_mode = "BASIC"
vocab_size = 20000
hidden_size = 400#20#需要修改
init_scale = 0.1
learning_rate = 1.0
max_grad_norm = 5
num_layers = 2
num_steps = 20#默认为20，之后会变为文件中句子最大长度
max_epoch = 4#14#
max_max_epoch = 13#131#55#需要修改
keep_prob = 0.3#1.0
keep_probs = {0.3,0.2,0.1}
lr_decay = 0.5#1 / 1.15#
batch_size = 20
