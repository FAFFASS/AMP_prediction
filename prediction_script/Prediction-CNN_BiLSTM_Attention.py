#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# usage python Prediction-CNN_BiLSTM_Attention.py XX.vec XX.pred_out

from keras.models import load_model
from numpy import loadtxt, savetxt
from Attention import AttentionLayer
from sys import argv

input_data_path = argv[1]
output_data_path = argv[2]
model = '../models/CNN_BiLSTM_Attention_model.h5'

model = load_model(model, custom_objects={'AttentionLayer': AttentionLayer})
input_data = loadtxt(input_data_path, delimiter=",")

pred = model.predict(input_data)
savetxt(output_data_path, pred, fmt="%.8f", delimiter=",")
