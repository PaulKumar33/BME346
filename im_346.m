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
corr10 = im_decomp('comp_2.jpg', 1);
corr20 = im_decomp('comp_3.jpg', 2);
corr30 = im_decomp('comp_4.jpg', 3);
corr40 = im_decomp('comp_5.jpg', 4);
corr50 = im_decomp('comp_6.jpg', 5);

corr11 = im_decomp('hek_1.jpg', 1);
corr21 = im_decomp('hek_2.jpg', 2);
corr31 = im_decomp('hek_3.jpg', 3);
corr41 = im_decomp('hek_4.jpg', 4);
corr51 = im_decomp('hek_5.jpg', 5);
corr61 = im_decomp('hek_composite1.jpg', 6);

%%      difference for hek images

diff_hek1 = im_diff('hek_1.jpg', 1);
diff_hek2 = im_diff('hek_2.jpg', 2);
diff_hek3 = im_diff('hek_3.jpg', 3);
diff_hek4 = im_diff('hek_4.jpg', 4);
diff_hek5 = im_diff('hek_5.jpg', 5);
diff_hek6 = im_diff('hek_composite1.jpg', 6);

%%      cross correlation for hek images 


%% processing the images into bar graphs

data_hela = [24, 3, 21;
             87, 3, 84;
             29, 7, 22;
             14, 7, 7
             56, 0, 56];
         
data_hela_error = [3, 0.5, 1;
                   11, 0.5, 10;
                   3, 1, 2;
                   2, 1, 1
                   7, 0, 7];
         
data_hek = [3, 1, 2;
            3, 1, 2;
            8, 5, 3;
            3, 1, 2;
            7, 7, 0;
            20, 6, 14
            18, 18, 0];

data_hek_error = [0.3, 0.1, 0.1;
                  0.3, 0.1, 0.1;
                  1, 0.2, 1;
                  0.1, 0.1, 0.05;
                  1, 1, 0;
                  3, 1, 1
                  2, 2, 0];
        
location = ['total cells', 'live cells', 'dead cells'];

ax = axes;
h = bar(data_hela, 'Barwidth', 1);

%properties of the bar
ax.YGrid = 'on';
ax.GridLineStyle = '-';
xticks(ax, [1 2 3]);

% naming each of the bar groups

%labels
xlabel('cell category');
ylabel('Cell count');

% creating legend
lg = legend('Total Cells', 'Live Cells', 'Dead Cells', "AutoUpdate", 'off');
lg.Location = 'BestOutside';
lg.Orientation = 'Horizontal';

hold on;

% finds the number of groups in bars
ngroups = size(data_hela, 1);
nbars = size(data_hela, 2);

% calculating the width for each bar
groupwidth = min(0.8, nbars/(nbars + 1.5));

for i = 1:nbars
    x = (1:ngroups) - groupwidth/2 + (2*i-1) * groupwidth/(2*nbars);
    errorbar(x, data_hela(:,i), data_hela_error(:,i));
end
hold off;
figure(2);

h2 = bar(data_hek, 'Barwidth', 1);
hold on;
ngroups2 = size(data_hek, 1);
nbars2 = size(data_hek, 2);

lg = legend('Total Cells', 'Live Cells', 'Dead Cells', "AutoUpdate", 'off');
lg.Location = 'BestOutside';
lg.Orientation = 'Horizontal';

groupwidth2 = min(0.8, nbars2/(nbars2 + 1.5));

legend('Total Cells', 'Dead Cells', 'Live Cells', 'Location', 'northwest')
title('HEK cell distribution')
ylabel('Cell count')

for i2 = 1:nbars2
    x2 = (1:ngroups2) - (groupwidth2)/2 + (2*i2 - 1) * (groupwidth2)/(2*nbars2);
    errorbar(x2, data_hek(:,i2), data_hek_error(:,i2));
end

%%

nax_array = [max(corr10(:)), max(corr11(:)), max(corr20(:)), max(corr21(:)), max(corr30(:)), max(corr31(:)), max(corr40(:)), max(corr41(:)), max(corr50(:)), max(corr51(:)), max(corr61(:))];
x = linspace(1,12,11);

%max of them occur at element 3 and 8
max_hela = nax_array(3);
max_hek = nax_array(8);

relative_max_hela = zeros(3);
relative_max_hek = zeros(6);
n1 = 0;
n2 = 0;

for i = 1:11
    if(i >= 1 && i <= 4)
        if(i ~= 3)
            n1 = n1 + 1;
            relative_max_hela(n1) = nax_array(i)/nax_array(3);
        end
    end
    
    if(i >= 5 && i <= 11)
        if(i~=7)
            n2 = n2 + 1;
            relative_max_hek(n2) = nax_array(i)/nax_array(7);
        end
    end
end

%%
new_hek = zeros(6,1);
new_hela = zeros(3,1);
for i = 1:9
    if(i <= 6)
        new_hek(i) = relative_max_hek(i,1);
    else
        new_hela(i) = relative_max_hela(i-6,1);
    end
end

[hh, ph] = ttest(new_hek(:));

[he, pe] = ttest(new_hela(:));




