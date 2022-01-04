-- Copyright 2014 Aedan Renner <chipdankly@gmail.com>
-- Copyright 2018 Florian Eckert <fe@dev.tdt.de>
-- Licensed to the public under the GNU General Public License v2.

local fs = require "nixio.fs"
local ut = require "luci.util"
local script = "/etc/mwan3.user"

local m, f, t

m = SimpleForm("luci", translate("Arca Load Balancing - Notification"))

f = m:section(SimpleSection, nil,
	translate(""))

t = f:option(TextValue, "lines")
t.rmempty = true
t.rows = 20
function t.cfgvalue()
	return fs.readfile(script)
end
function t.write(self, section, data)
	return fs.writefile(script, ut.trim(data:gsub("\r\n", "\n")) .. "\n")
end

return m
