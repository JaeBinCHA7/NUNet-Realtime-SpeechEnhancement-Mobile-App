#################################################################################
#  configuration
#################################################################################
BATCH_SIZE = None
EPOCH = None
learning_rate = 0.001
#################################################################################
#  STFT
#################################################################################
win_len = 512
stride = 128
fft_len = 512
fs = 16000
#################################################################################
#  Data Loader
#################################################################################
path_to_train_noisy = None
path_to_train_clean = None
path_to_val_noisy = None
path_to_val_clean = None

#################################################################################
#  Path
#################################################################################
file_name = None
saved_model_dir = 'saved_model/'
logdir = 'logs/'
logfile = logdir + file_name
chpt_dir = 'checkpoint/' + file_name[:-3]