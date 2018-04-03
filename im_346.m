im = imread('comp_2.jpg');

red = im(:,:,1);
blue = im(:,:,3);
[x, y] = meshgrid(0:2782, 0:2078);
corr = xcorr2(red, blue);
h = surf(x,y,corr);
set(h, 'Linestyle', 'none')

colorbar

%%
corr2 = im_decomp('comp_3.jpg');
[x, y] = meshgrid(0:2782, 0:2078);
h = surf(x,y,corr2);
set(h, 'Linestyle', 'none')
colorbar

%%
corr3 = im_decomp('comp_4.jpg');
[x, y] = meshgrid(0:2782, 0:2078);
h = surf(x,y,corr3);
set(h, 'Linestyle', 'none')
colorbar



%%
corr4 = im_decomp('comp_5.jpg');
[x, y] = meshgrid(0:2782, 0:2078);
h = surf(x,y,corr4);
set(h, 'Linestyle', 'none')
colorbar

%%
corr5 = im_decomp('comp_6.jpg');
[x, y] = meshgrid(0:2782, 0:2078);
h = surf(x,y,corr5);
set(h, 'Linestyle', 'none')
colorbar


%%     calculates all the differences in pixel
diff1 = im_diff('comp_2.jpg', 1);
diff2 = im_diff('comp_3.jpg', 2);
diff3 = im_diff('comp_4.jpg', 3);
diff4 = im_diff('comp_5.jpg', 4);
diff5 = im_diff('comp_6.jpg', 5);

%%      calculates cross correlation
corr1 = im_decomp('comp_2.jpg', 1);
corr2 = im_decomp('comp_3.jpg', 2);
corr3 = im_decomp('comp_4.jpg', 3);
corr4 = im_decomp('comp_5.jpg', 4);
corr5 = im_decomp('comp_6.jpg', 5);

%%      difference for hek images

diff_hek1 = im_diff('hek_1.jpg', 1);
diff_hek2 = im_diff('hek_2.jpg', 2);
diff_hek3 = im_diff('hek_3.jpg', 3);
diff_hek4 = im_diff('hek_4.jpg', 4);
diff_hek5 = im_diff('hek_5.jpg', 5);
diff_hek6 = im_diff('hek_composite1.jpg', 6);

%%      cross correlation for hek images 
corr1 = im_decomp('hek_1.jpg', 1);
corr2 = im_decomp('hek_2.jpg', 2);
corr3 = im_decomp('hek_3.jpg', 3);
corr4 = im_decomp('hek_4.jpg', 4);
corr5 = im_decomp('hek_5.jpg', 5);
corr6 = im_decomp('hek_composite1.jpg', 6);