dir = 'E:\mestrado\face-recognition\gabor\';

fileRead1 = strcat(dir,'filtro_Curvo_PCA_Histograma_PCA_iluminacaiiculos_meiopi_0_ARface_100_4_4x4_5x8_15x15.txt');
fileRead2 = strcat(dir,'filtro_Curvo_PCA_Histograma_PCA_iluminacaiiculos_meiopi_0.05_ARface_100_4_4x4_5x16_15x15.txt');
fileRead3 = strcat(dir,'filtro_Curvo_PCA_Histograma_PCA_iluminacaiiculos_meiopi_0.1_ARface_100_4_4x4_5x16_15x15.txt');
fileRead4 = strcat(dir,'filtro_Curvo_PCA_Histograma_PCA_iluminacaiiculos_meiopi_0.2_ARface_100_4_4x4_5x16_15x15.txt');
num=1000;

filesTrain = [
    sprintf('%-*s', num, fileRead1);
    sprintf('%-*s', num, fileRead2);
    sprintf('%-*s', num, fileRead3);
    sprintf('%-*s', num, fileRead4)
    ];
% 
% fileRead01 = strcat(dir,'hist_gabor_curvo_0.00_oclusao_100_12_8x8_5x8_30x30.txt');
% fileRead02 = strcat(dir,'hist_gabor_curvo_0.05_oclusao_100_12_8x8_5x16_30x30.txt');
% fileRead03 = strcat(dir,'hist_gabor_curvo_0.1_oclusao_100_12_8x8_5x16_30x30.txt');
% fileRead04 = strcat(dir,'hist_gabor_curvo_0.2_oclusao_100_12_8x8_5x16_30x30.txt');
% 
% filesTest = [
%     sprintf('%-*s', num, fileRead01);
%     sprintf('%-*s', num, fileRead02);
%     sprintf('%-*s', num, fileRead03);
%     sprintf('%-*s', num, fileRead04)
%     ];

%for j=2000:500:10000
    heart_scale_instreino=[];
    heart_scale_labeltreino=[];
    heart_scale_insteste=[];
    heart_scale_labelteste=[];
    clearvars heart_scale_inst1 heart_scale_label1 red_dim;
    
    for i = 1:4
       % disp(j);
        disp(strtrim(filesTrain(i,:)));
        [heart_scale_label1, heart_scale_inst1] = libsvmread(strtrim(filesTrain(i,:)));
        heart_scale_inst1 = full(heart_scale_inst1);
        %um = zeros(size(heart_scale_inst1,1),20);
        %heart_scale_inst1 = horzcat(heart_scale_inst1,um);
        %[pc,score,latent,tsquare] = princomp(heart_scale_inst1);
        
        %red_dim = score(:,1:j);
        heart_scale_instreino = horzcat(heart_scale_instreino,heart_scale_inst1);

        %clearvars heart_scale_inst1 heart_scale_label1 red_dim;
        disp('--------------------------------LIDO--------------------------------------');
    end
%     name = strcat('hist_gabor_curvo_TOTAL_test2_crop_100_14_8x8_5x16_30x30_', num2str(j) ,'.txt');
%     libsvmwrite(name, heart_scale_labeltreino, sparse(heart_scale_instreino));
    
%     for i = 1:4
%         %disp(j);
%         disp(strtrim(filesTest(i,:)));
%         [heart_scale_label1, heart_scale_inst1] = libsvmread(strtrim(filesTest(i,:)));
%         heart_scale_inst1 = full(heart_scale_inst1);
%         
%         [pc,score,latent,tsquare] = princomp(heart_scale_inst1);
%         red_dim = score(:,1:j);
%         heart_scale_insteste = [heart_scale_insteste; red_dim];
%         heart_scale_labelteste = [heart_scale_labelteste; heart_scale_label1];
%         clearvars heart_scale_inst1 heart_scale_label1 red_dim
%         disp('--------------------------------LIDO--------------------------------------');
%         
%     end
%     
    name = strcat('hist_gabor_curvo_TOTAL_cacheco2_meiopi_', num2str(i) ,'.txt');
     libsvmwrite(name, heart_scale_label1, sparse(heart_scale_instreino));
%     
%     disp('treinando')
%     model = svmtrain(heart_scale_labeltreino, heart_scale_instreino);
%     disp('--------------------------------TREINADO--------------------------------------');
%     [predict_label, accuracy, dec_values] = svmpredict(heart_scale_labelteste, heart_scale_insteste, model);
%     disp('--------------------------------PREDITO---------------------------------------');
%     fileID = fopen('resultado.txt','a');
%     fprintf(fileID, strcat(num2str(accuracy), '_',num2str(j), '\n'));
%     fclose(fileID);
%     disp('--------------------------------FIM--------------------------------------');
%end