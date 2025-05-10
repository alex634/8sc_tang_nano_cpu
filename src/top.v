module top
(
    input rst,
    input clk,
    input button,
    output [5:0] leds
);

wire [5:0] raw_leds;

wire [7:0] negator_output;
wire [7:0] pc_counter_adder_a;
wire [7:0] pc_counter_adder_out;
wire [7:0] pc_counter_out;
wire take_Branch;

wire [7:0] current_instruction;

wire branch;
wire ldh;
wire rd_ram;
wire ldc;
wire w_ram;
wire w_reg;
wire [1:0] op;

wire [7:0] read1;
wire [7:0] read2;

wire gt;
wire last_cycle_gt;

wire [7:0] alu_output;

wire [7:0] r_data;

wire [1:0] parsed_reg1;
wire [1:0] parsed_reg1_alt;
wire [1:0] parsed_reg2;
wire parsed_Direction;
wire [3:0] parsed_constant;

wire [6:0] negator_input;

wire [7:0] ldh_constant;
wire [7:0] ldl_constant;
wire [7:0] ldc_value;

wire [1:0] reg1;
wire [7:0] alu_output_or_r_data;
wire [7:0] w_data;

assign pc_counter_adder_a = (take_Branch) ? negator_output: 1;
assign pc_counter_adder_out = pc_counter_adder_a + pc_counter_out;
assign take_Branch = branch & last_cycle_gt;

assign parsed_reg1 = current_instruction[4:3];
assign parsed_reg2 = current_instruction[2:1];
assign parsed_reg1_alt = {1'b0, parsed_direction};

assign parsed_direction = current_instruction[4];
assign parsed_constant = current_instruction[3:0];
assign ldh_constant = {parsed_constant, read1[3:0]};
assign ldl_constant = {read1[7:4], parsed_constant};
assign ldc_value = (ldh) ? ldh_constant: ldl_constant;

assign negator_input = {3'b000, parsed_constant};
assign reg1 = (ldc) ? parsed_reg1_alt: parsed_reg1;

assign alu_output_or_r_data = (rd_ram) ? r_data: alu_output;
assign w_data = (ldc) ? ldc_value: alu_output_or_r_data;
assign leds = ~raw_leds;

d_register #(.WIDTH(8)) pc_counter (.d(pc_counter_adder_out), .q(pc_counter_out), .rst(rst), .clk(clk));

d_flipflop gt_flipflop (.d(gt), .q(last_cycle_gt), .rst(rst), .clk(clk));

memory #(.WORD_SIZE(8), .ADDRESS_SIZE(8)) data_memory (.addr(read2), .r_data(r_data), .w_data(read1), .w_en(w_ram), .rst(rst), .clk(clk), .leds(raw_leds), .button(button));

instruction_rom instruction_memory (.addr(pc_counter_out), .data(current_instruction));

alu #(.WIDTH(8)) main_alu (.a(read1),.b(read2),.c(alu_output), .op(op), .gt(gt));

negator #(.INPUT_WIDTH(7)) negate (.in(negator_input), .en(parsed_direction), .out(negator_output));

control_unit cu (.instruction(current_instruction[7:5]), .op(op), .branch(branch), .ldh(ldh), .rd_ram(rd_ram), .ldc(ldc), .w_reg(w_reg), .w_ram(w_ram));

register_file #(.DATA_WIDTH(8), .REGISTER_ID_WIDTH(2)) registers (.reg1(reg1), .reg2(parsed_reg2), .w_reg(reg1), .w_data(w_data), .w_en(w_reg), .clk(clk), .rst(rst), .read1(read1), .read2(read2));


endmodule
