module memory
#(
parameter WORD_SIZE = 8,
parameter ADDRESS_SIZE = 8
)

(
input [ADDRESS_SIZE - 1 : 0] addr,
output [WORD_SIZE - 1 : 0] r_data,
input [WORD_SIZE - 1 : 0] w_data,
input w_en,
input rst,
input clk,
output [5:0] leds,
input button
);

integer i;

reg [WORD_SIZE - 1 : 0] mem [0 : 2**ADDRESS_SIZE - 2];

assign r_data = (addr != 2**ADDRESS_SIZE - 1) ? mem[addr]: {7'b0000000, button};

assign leds = {mem[2**ADDRESS_SIZE - 2][0],mem[2**ADDRESS_SIZE - 3][0],mem[2**ADDRESS_SIZE - 4][0],mem[2**ADDRESS_SIZE - 5][0],mem[2**ADDRESS_SIZE - 6][0], mem[2**ADDRESS_SIZE - 7][0]};

always @ (posedge clk or posedge rst) begin
    if (rst) begin
        for (i = 0; i < 2**ADDRESS_SIZE - 1; i = i + 1) begin
            mem[i] = 0;
        end
    end 
    else begin
        if (w_en) begin
            if (addr != 2**ADDRESS_SIZE - 1)
                mem[addr] = w_data;
        end
    end
end

endmodule
