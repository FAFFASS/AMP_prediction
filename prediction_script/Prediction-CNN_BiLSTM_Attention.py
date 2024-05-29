#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# usage python Prediction_attention.py XX.vec XX.pred_out

from keras.models import load_model
from numpy import loadtxt, savetxt
from Attention import AttentionLayer
from sys import argv

input_data_path = 'XX.vec--'
output_data_path = 'XX.pred_out'
model = '../models/CNN_BiLSTM_Attention_model.h5'

model = load_model(model, custom_objects={'AttentionLayer': AttentionLayer})
input_data = loadtxt(input_data_path, delimiter=",")

pred = model.predict(input_data)
savetxt(output_data_path, pred, fmt="%.8f", delimiter=",")
