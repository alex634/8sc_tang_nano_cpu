module d_register

#(
    parameter WIDTH = 8
)

(
    input [WIDTH - 1 : 0] d ,
    input clk,
    input rst,
    output reg [WIDTH - 1 : 0] q
);

always @ (posedge clk or posedge rst) begin
    if (rst)
        q = 0;
    else
        q = d;
end

endmodule
