function res = im_diff(location, n)
    im = imread(location);
    red = im(:,:,1);
    blue = im(:,:,3);
    
    res = blue - red;
    [xr, yr] = meshgrid(0:1391, 0:1039);
    
    figure(n);
    h = surf(xr,yr,res);
    set(h, 'Linestyle', 'none')
    xlabel('pixel location')
    ylabel('pixel location')
    zlabel('Pixel Difference')
    
    colorbar
end