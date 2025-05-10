module register_file
#
(
parameter DATA_WIDTH = 8,
parameter REGISTER_ID_WIDTH = 2
)

(
    input [REGISTER_ID_WIDTH - 1 : 0] reg1,
    input [REGISTER_ID_WIDTH - 1 : 0] reg2,
    input [REGISTER_ID_WIDTH - 1 : 0] w_reg,
    input [DATA_WIDTH - 1 : 0] w_data,
    input w_en,
    input clk,
    input rst,
    output [DATA_WIDTH - 1 : 0] read1,
    output [DATA_WIDTH - 1 : 0] read2
);

reg [DATA_WIDTH - 1 : 0] data [0 : 2**REGISTER_ID_WIDTH - 1];
integer i;

assign read1 = data [reg1];
assign read2 = data [reg2];

always @ (posedge clk or posedge rst) begin
    if (rst)
    begin
        for (i = 0; i < 2**REGISTER_ID_WIDTH; i = i + 1) begin
            data[i] = 0;
        end
    end else 
    begin
        if (w_en)
            data [w_reg] = w_data;
    end 
end

endmodule
