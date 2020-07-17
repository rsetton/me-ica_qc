# me-ica_qc
Quality checking for ME-ICA processed ME data.

<b>Preface:</b> this is a super clunky (but usable!) script that pastes together typical QC steps for any fMRI data and outputs a pdf report for easy viewing. The hope is to return to this and make it more generalizable. For now please use and adapt as you see fit.

<b>Requirements (for now):</b>
<br>
-ME-ICA processed data
<br>
-afni
<br>
-fsl
<br>
-python
<br>
-ImageMagick (but not necessary if not generating pdf report)


<b>Returns:</b>
<br>
-co-registration assessment as a jpeg with various sagittal slices
<br>
-# of accepted, rejected, midk, and total components identified in txt and jpeg formats
<br>
-plot of 6 motion parameters as a jpeg
<br>
-fd and dvars for the timeseries as txt files, plots, and outlier matrices
<br>
-a comparison of DVARS for various outputs (tsoc, lowk, hik, and medn) as a jpeg
<br>
-tsnr maps of medn outpus in native space and screen shots
<br>
-a pdf report containing all of the above


<b>References:</b>
Steps are largely based off public notes from the Cambridge group wiki (https://wiki.cam.ac.uk/bmuwiki/Matilde_QC).
