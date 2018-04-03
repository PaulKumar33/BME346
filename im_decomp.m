function matrix = im_decomp(location, n)
    im = imread(location);
    red = im(:,:,1);
    blue = im(:,:,3);
    corr = xcorr2(red, blue);
    matrix = corr;
    
    [xm, ym] = meshgrid(0:2782, 0:2078);

    figure(n);
    h = surf(xm, ym, matrix);
    set(h, 'Linestyle', 'none')
    
    xlabel('relative x pixel shift')
    ylabel('relative y pixel shift')
    zlabel('cross correlation intensity')
    colorbar
    
end