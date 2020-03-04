library IEEE;
use IEEE.STD_LOGIC_1164.ALL;
 
entity bcd_7segment is
Port ( BCDin : in STD_LOGIC_VECTOR (3 downto 0);
Seven_Segment : out STD_LOGIC_VECTOR (6 downto 0));
end bcd_7segment;
 
architecture Behavioral of bcd_7segment is
 
begin
 
process(BCDin)
begin
 
case BCDin is
when "0000" =>
Seven_Segment <= "0000001"; ---0
when "0001" =>
Seven_Segment <= "1001111"; ---1
when "0010" =>
Seven_Segment <= "0010010"; ---2
when "0011" =>
Seven_Segment <= "0000110"; ---3
when "0100" =>
Seven_Segment <= "1001100"; ---4
when "0101" =>
Seven_Segment <= "0100100"; ---5
when "0110" =>
Seven_Segment <= "0100000"; ---6
when "0111" =>
Seven_Segment <= "0001111"; ---7
when "1000" =>
Seven_Segment <= "0000000"; ---8
when "1001" =>
Seven_Segment <= "0000100"; ---9
when others =>
Seven_Segment <= "1111111"; ---null
end case;
 
end process;
 
end Behavioral;

LIBRARY ieee;
USE ieee.std_logic_1164.ALL;
 
ENTITY tb_bcd_7seg IS
END tb_bcd_7seg;
 
ARCHITECTURE behavior OF tb_bcd_7seg IS
 
-- Component Declaration for the Unit Under Test (UUT)
 
COMPONENT bcd_7segment
PORT(
BCDin : IN std_logic_vector(3 downto 0);
Seven_Segment : OUT std_logic_vector(6 downto 0)
);
END COMPONENT;
 
--Inputs
signal BCDin : std_logic_vector(3 downto 0) := (others => '0');
 
--Outputs
signal Seven_Segment : std_logic_vector(6 downto 0);
 
BEGIN
 
-- Instantiate the Unit Under Test (UUT)
uut: bcd_7segment PORT MAP (
BCDin => BCDin,
Seven_Segment => Seven_Segment
);
 
-- Stimulus process
stim_proc: process
begin
 
BCDin <= "0100";
wait for 100 ns;
end process;
 
END;
