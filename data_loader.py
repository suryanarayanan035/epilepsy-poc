#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 13:25:38 2021

@author: suryanarayanan

"""
import mne
eeg_file = mne.io.read_raw_edf("chb01_01.edf")
eeg_file.plot(duration=2,n_channels=2,bgcolor="blue")
