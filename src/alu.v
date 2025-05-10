module alu 

# 
(
    parameter WIDTH = 8
)

(
    input wire [WIDTH - 1 : 0] a,
    input wire [WIDTH - 1 : 0] b,
    output reg [WIDTH - 1 : 0] c,
    input wire [1:0] op,
    output wire gt
);



assign gt = a > b;

always @ (a or b or op) begin
    case (op)
        2'b00: c = a + b;
        2'b01: c = ~(a & b);
        default: c = a >> b;
    endcase
end

endmodule
