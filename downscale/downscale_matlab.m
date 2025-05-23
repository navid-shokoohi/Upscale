% Load your hyperspectral cube
load('sample.mat'); % variable is "cube"

% Define scale factor
scale = 0.5;

% Get original size
[height, width, bands] = size(cube);

% Preallocate downscaled cube
downscaled_cube = zeros(round(height*scale), round(width*scale), bands, 'like', cube);

% Resize each spectral band
for b = 1:bands
    downscaled_cube(:,:,b) = imresize(cube(:,:,b), scale, 'bicubic');
end

save('sample_downscale.mat', 'downscaled_cube');

fprintf('Downscaled: %d x %d x %d\n', size(downscaled_cube,1), size(downscaled_cube,2), size(downscaled_cube,3));
