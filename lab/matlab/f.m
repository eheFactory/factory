clc;
close all;
clear all;


imgName ="r.jpg";
rgbi = imread(imgName);
% rgbi = imresize(rgbi, [1024 768]);

[rows, columns, numberOfColorBands] = size(rgbi);

% figure
% imshow(rgbi);


bwi=im2bw(rgbi);

% figure
% imshow(bwi);

s = size(bwi);

sx = s(1);
sy = s(2);
w = 1;

fc = fopen('sws.txt', 'w');
for i = 1:sx
    for j = 1:sy
        
        if bwi(i,j) == 0
            formatSpec = '{x: %f, y:%f}, \n';
            fprintf(fc, formatSpec, i+0.5, j+0.5);
        end
    end
end

fclose(fc);



y = fft2(bwi);

p2 = uint8(ifft2(y));
figure
imagesc(uint8(p2));


