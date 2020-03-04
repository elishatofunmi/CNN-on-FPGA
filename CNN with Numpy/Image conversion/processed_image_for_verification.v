/****************** Module for writing .bmp image *************/ 
/***********************************************************/ 
// fpga4student.com FPGA projects, Verilog projects, VHDL projects
// Verilog project: Image processing in Verilog
module image_write #(parameter 
WIDTH = 768, // Image width 
HEIGHT = 512, // Image height 
INFILE = "output.bmp", // Output image 
BMP_HEADER_NUM = 54 // Header for bmp image 
) 
( 
input HCLK, // Clock input 
HRESETn, // Reset active low 
input hsync, // Hsync pulse 
input [7:0] DATA_WRITE_R0, // Red 8-bit data (odd) 
input [7:0] DATA_WRITE_G0, // Green 8-bit data (odd) 
input [7:0] DATA_WRITE_B0, // Blue 8-bit data (odd) 
input [7:0] DATA_WRITE_R1, // Red 8-bit data (even) 
input [7:0] DATA_WRITE_G1, // Green 8-bit data (even) 
input [7:0] DATA_WRITE_B1, // Blue 8-bit data (even) 
output reg Write_Done 
); 
// fpga4student.com FPGA projects, Verilog projects, VHDL projects
//-----------------------------------// 
//-------Header data for bmp image-----// 
//-------------------------------------// 
// Windows BMP files begin with a 54-byte header
initial  begin 
BMP_header[ 0] = 66;BMP_header[28] =24; 
BMP_header[ 1] = 77;BMP_header[29] = 0; 
BMP_header[ 2] = 54;BMP_header[30] = 0; 
BMP_header[ 3] = 0;BMP_header[31] = 0;
BMP_header[ 4] = 18;BMP_header[32] = 0;
BMP_header[ 5] = 0;BMP_header[33] = 0; 
BMP_header[ 6] = 0;BMP_header[34] = 0; 
BMP_header[ 7] = 0;BMP_header[35] = 0; 
BMP_header[ 8] = 0;BMP_header[36] = 0; 
BMP_header[ 9] = 0;BMP_header[37] = 0; 
BMP_header[10] = 54;BMP_header[38] = 0; 
BMP_header[11] = 0;BMP_header[39] = 0; 
BMP_header[12] = 0;BMP_header[40] = 0; 
BMP_header[13] = 0;BMP_header[41] = 0; 
BMP_header[14] = 40;BMP_header[42] = 0; 
BMP_header[15] = 0;BMP_header[43] = 0; 
BMP_header[16] = 0;BMP_header[44] = 0; 
BMP_header[17] = 0;BMP_header[45] = 0; 
BMP_header[18] = 0;BMP_header[46] = 0; 
BMP_header[19] = 3;BMP_header[47] = 0;
BMP_header[20] = 0;BMP_header[48] = 0;
BMP_header[21] = 0;BMP_header[49] = 0; 
BMP_header[22] = 0;BMP_header[50] = 0; 
BMP_header[23] = 2;BMP_header[51] = 0; 
BMP_header[24] = 0;BMP_header[52] = 0; 
BMP_header[25] = 0;BMP_header[53] = 0; 
BMP_header[26] = 1; BMP_header[27] = 0; 
end
//---------------------------------------------------------//
//--------------Write .bmp file  ----------------------//
//----------------------------------------------------------//
initial begin
    fd = $fopen(INFILE, "wb+");
end
always@(Write_Done) begin // once the processing was done, bmp image will be created
    if(Write_Done == 1'b1) begin
        for(i=0; i<BMP_HEADER_NUM; i=i+1) begin
            $fwrite(fd, "%c", BMP_header[i][7:0]); // write the header
        end
        
        for(i=0; i<WIDTH*HEIGHT*3; i=i+6) begin
  // write R0B0G0 and R1B1G1 (6 bytes) in a loop
            $fwrite(fd, "%c", out_BMP[i  ][7:0]);
            $fwrite(fd, "%c", out_BMP[i+1][7:0]);
            $fwrite(fd, "%c", out_BMP[i+2][7:0]);
            $fwrite(fd, "%c", out_BMP[i+3][7:0]);
            $fwrite(fd, "%c", out_BMP[i+4][7:0]);
            $fwrite(fd, "%c", out_BMP[i+5][7:0]);
        end
    end
end