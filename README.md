# me-ica_qc
Quality checking for ME-ICA processed ME data.

Preface: this is a super clunky (but usable!) script that pastes together typical QC steps for any fMRI data and outputs a pdf report for easy viewing. The hope is to return to this and make it more generalizable. For now please use and adapt as you see fit.

Requirements (for now):
-ME-ICA processed data
-afni
-fsl
-python
-ImageMagick (but not necessary if not generating pdf report)


Returns: 
-co-registration assessment as a jpeg with various sagittal slices
-# of accepted, rejected, midk, and total components identified in txt and jpeg formats
-plot of 6 motion parameters as a jpeg
-fd and dvars for the timeseries as txt files, plots, and outlier matrices
-a comparison of DVARS for various outputs (tsoc, lowk, hik, and medn) as a jpeg
-tsnr maps of medn outpus in native space and screen shots
-a pdf report containing all of the above


References:
Steps are largely based off public notes from the Cambridge group wiki (https://wiki.cam.ac.uk/bmuwiki/Matilde_QC).
