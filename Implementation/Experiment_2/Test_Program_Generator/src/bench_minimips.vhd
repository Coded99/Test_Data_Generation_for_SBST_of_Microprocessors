------------------------------------------------------------------------------------
--                                                                                --
--    Copyright (c) 2004, Hangouet Samuel                                         --
--                  , Jan Sebastien                                               --
--                  , Mouton Louis-Marie                                          --
--                  , Schneider Olivier     all rights reserved                   --
--                                                                                --
--    This file is part of miniMIPS.                                              --
--                                                                                --
--    miniMIPS is free software; you can redistribute it and/or modify            --
--    it under the terms of the GNU Lesser General Public License as published by --
--    the Free Software Foundation; either version 2.1 of the License, or         --
--    (at your option) any later version.                                         --
--                                                                                --
--    miniMIPS is distributed in the hope that it will be useful,                 --
--    but WITHOUT ANY WARRANTY; without even the implied warranty of              --
--    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the               --
--    GNU Lesser General Public License for more details.                         --
--                                                                                --
--    You should have received a copy of the GNU Lesser General Public License    --
--    along with miniMIPS; if not, write to the Free Software                     --
--    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA   --
--                                                                                --
------------------------------------------------------------------------------------


-- If you encountered any problem, please contact :
--
--   lmouton@enserg.fr
--   oschneid@enserg.fr
--   shangoue@enserg.fr
--


library IEEE;
use IEEE.std_logic_1164.all;

library std;
use std.textio.all;

library work;
use work.my_package.all;

library minimips_rtl;
use minimips_rtl.pack_mips.all;

entity sim_minimips is
end;

architecture bench of sim_minimips is

   constant threshold : integer := 21;

  component minimips is
  port (
      clock    : in std_logic;
      reset    : in std_logic;

      ram_req  : out std_logic;
      ram_adr  : out bus32;
      ram_r_w  : out std_logic;
      ram_data : inout bus32;
      ram_ack  : in std_logic;
      it_mat   : in std_logic
  );
  end component;


  component ram is
    generic (mem_size : natural := 65536;
             latency : time := 50 ns);  -- 10ns  at RTL level
    port(
        req        : in std_logic;
        adr        : in bus32;
        data_inout : inout bus32;
        r_w        : in std_logic;
        ready      : out std_logic
  );
  end component;

  component rom is
  generic (mem_size : natural := 65536;
           start : natural := 0;
           latency : time := 50 ns);   -- 10ns  at RTL level
  port(
          adr : in bus32;
          donnee : out bus32;
          ack : out std_logic;
          load : in std_logic;
          fname : in string
  );
  end component;


component renvoi is
  port (
      adr1 : in adr_reg_type;
      adr2 : in adr_reg_type;
      use1 : in std_logic;
      use2 : in std_logic;
      data1 : out bus32;
      data2 : out bus32;
      alea : out std_logic;
      DI_level : in level_type;
      DI_adr : in adr_reg_type;
      DI_ecr : in std_logic;
      DI_data : in bus32;
      EX_level : in level_type;
      EX_adr : in adr_reg_type;
      EX_ecr : in std_logic;
      EX_data : in bus32;
      MEM_level : in level_type;
      MEM_adr : in adr_reg_type;
      MEM_ecr : in std_logic;
      MEM_data : in bus32;
      interrupt : in std_logic;
      write_data : out bus32;
      write_adr : out bus5;
      write_GPR : out std_logic;
      write_SCP : out std_logic;
      read_adr1 : out bus5;
      read_adr2 : out bus5;
      read_data1_GPR : in bus32;
      read_data2_GPR : in bus32;
      read_data1_SCP : in bus32;
      read_data2_SCP : in bus32
  );
end component;

  signal clock : std_logic := '0';
  signal reset : std_logic;

  signal it_mat : std_logic := '0';

  -- Connexion with the code memory
  signal load : std_logic;
  signal rom_file : string(1 to 7) := "rom.bin";

  -- Connexion with the Ram
  signal ram_req : std_logic;
  signal ram_adr : bus32;
  signal ram_r_w : std_logic;
  signal ram_data : bus32;
  signal ram_rdy : std_logic;

  signal end_sim : std_logic := '0';

  -- connection with renvoi
  signal adr1 : adr_reg_type;
  signal adr2 : adr_reg_type;
  signal use1 : std_logic;
  signal use2 : std_logic;
  signal data1 : bus32;
  signal data2 : bus32;
  signal alea : std_logic;
  signal DI_level : level_type;
  signal DI_adr : adr_reg_type;
  signal DI_ecr : std_logic;
  signal DI_data : bus32;
  signal EX_level : level_type;
  signal EX_adr : adr_reg_type;
  signal EX_ecr : std_logic;
  signal EX_data : bus32;
  signal MEM_level : level_type;
  signal MEM_adr : adr_reg_type;
  signal MEM_ecr : std_logic;
  signal MEM_data : bus32;
  signal interrupt : std_logic;
  signal write_data : bus32;
  signal write_adr :  bus5;
  signal write_GPR :  std_logic;
  signal write_SCP :  std_logic;
  signal read_adr1 :  bus5;
  signal read_adr2 :  bus5;
  signal read_data1_GPR : bus32;
  signal read_data2_GPR : bus32;
  signal read_data1_SCP : bus32;
  signal read_data2_SCP : bus32;

begin

    U_minimips : minimips port map (
        clock => clock,
        reset => reset,
        ram_req => ram_req,
        ram_adr => ram_adr,
        ram_r_w => ram_r_w,
        ram_data => ram_data,
        ram_ack => ram_rdy,
        it_mat => it_mat
    );

    U_ram : ram port map (
        req => ram_req,
        adr => ram_adr,
        data_inout => ram_data,
        r_w => ram_r_w,
        ready => ram_rdy
    );

    U_rom : rom port map (
      adr    => ram_adr,
      donnee => ram_data,
      ack    => ram_rdy,
      load   => load,
      fname  => rom_file
      );

  U_revoi: renvoi port map
  (
    adr1          =>  adr1,
    adr2          =>  adr2,
    use1          =>  use1,
    use2          =>  use2,
    data1         =>  data1,
    data2         =>  data2,
    alea          =>  alea,
    DI_level      =>  DI_level,
    DI_adr       =>  DI_adr,
    DI_ecr       =>  DI_ecr,
    DI_data      =>  DI_data,
    EX_level      =>  EX_level,
    EX_adr        =>  EX_adr,
    EX_ecr        =>   EX_ecr,
    EX_data       =>  EX_data,
    MEM_level     =>  MEM_level,
    MEM_adr      =>  MEM_adr,
    MEM_ecr      =>  MEM_ecr,
    MEM_data     =>  MEM_data,
    interrupt    =>  interrupt,
    write_data    =>  write_data,
    write_adr     =>  write_adr,
    write_GPR     =>  write_GPR,
    write_SCP     =>  write_SCP,
    read_adr1     =>  read_adr1,
    read_adr2     =>  read_adr2,
    read_data1_GPR =>  read_data1_GPR,
    read_data2_GPR =>  read_data2_GPR,
    read_data1_SCP =>  read_data1_SCP,
    read_data2_SCP =>  read_data2_SCP
  );

    clock <= not clock after 100 ns;    -- 20 ns at RTL level
    reset <= '0', '1' after 25 ns, '0' after 350 ns;
    --ram_data <= (others => 'L');

    load <= '1', '0' after 25 ns;


    -- Memory Mapping
    -- 0000 - 00FF      ROM

    process (ram_adr, ram_r_w, ram_data)
    begin -- Emulation of an I/O controller
        ram_data <= (others => 'Z');

        case ram_adr is
            when X"00002000" => -- program an interrupt after 1000ns
                                it_mat <= '1' after 1000 ns;
                                ram_rdy <= '1' after 5 ns;
            when X"00002001" => -- clear interrupt line on cpu
                                it_mat <= '0';
                                ram_data <= X"FFFFFFFF";
                                ram_rdy <= '1' after 5 ns;
            when others      => ram_rdy <= 'L';
        end case;
    end process;

-- write memory content to file
process (ram_rdy, ram_r_w, ram_data)
  file out_file : text open write_mode is "out.txt";
  variable line_v : line;
  begin
    if (ram_r_w = '1' and ram_rdy = '1') then
      write (line_v, to_bstring(ram_data));
      writeline(out_file, line_v);
    end if;
    --file_close(out_file);
end process;

-- STOP SIMULATION PROCESS
process (clock, reset)
   variable ram_adr_bak : bus32;
   variable count : integer;
begin
   if reset = '1' then

      ram_adr_bak := (others => '0');
      count := 0;

   elsif clock'event and clock='1' then

      if ram_adr_bak = ram_adr then
         count := count + 1;
      else
         count := 0;
         ram_adr_bak := ram_adr;
      end if;

      if count > threshold then
--          print("ENDSIM_ADDRESS: " & hstr(ram_adr));
--          print("ENDSIM_TIME: " & time'image(now));
         end_sim <= '1';
      end if;

   end if;
end process;


end bench;
