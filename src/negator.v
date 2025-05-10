module negator
#(
parameter INPUT_WIDTH = 7
)

(
input [INPUT_WIDTH - 1 : 0] in,
input  en,
output [INPUT_WIDTH : 0] out
);

assign out = (en) ? ( (~{1'b0,in}) + 1 ): {1'b0, in}; 

endmodule
