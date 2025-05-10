module control_unit

(
input [2:0] instruction,
output [1:0] op,
output branch,
output ldh,
output rd_ram,
output ldc,
output w_reg,
output w_ram
);

assign op = rom_output[7:6];
assign branch = rom_output[5];
assign ldh = rom_output[4];
assign rd_ram = rom_output[3];
assign ldc = rom_output[2];
assign w_reg = rom_output[1];
assign w_ram = rom_output[0];

reg [7:0] rom_output;

always @ (instruction) begin
    case (instruction)
        0: rom_output = 8'b00000010;
        1: rom_output = 8'b01000010;
        2: rom_output = 8'b10000010;
        3: rom_output = 8'b00100000;
        4: rom_output = 8'b00001010;
        5: rom_output = 8'b00000001;
        6: rom_output = 8'b00000110;
        7: rom_output = 8'b00010110;
    endcase
end

endmodule
