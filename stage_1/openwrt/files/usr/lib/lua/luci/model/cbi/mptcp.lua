local net = require "luci.model.network".init()
local sys = require "luci.sys"
local ifaces = sys.net:devices()
local m, s, o
local uname = nixio.uname()

m = Map("network", translate("Arca TCP"))

local unameinfo = nixio.uname() or { }

s = m:section(TypedSection, "globals")
o = s:option(ListValue, "multipath", translate("Arca TCP"))
o:value("enable", translate("enable"))
o:value("disable", translate("disable"))
o = s:option(ListValue, "mptcp_checksum", translate("Arca TCP checksum"))
o:value(1, translate("enable"))
o:value(0, translate("disable"))
o = s:option(ListValue, "mptcp_debug", translate("Debug"))
o:value(1, translate("enable"))
o:value(0, translate("disable"))
o = s:option(ListValue, "mptcp_path_manager", translate("Path-manager"), translate("Default is fullmesh"))
o:value("default", translate("default"))
o:value("fullmesh", "fullmesh")
o:value("ndiffports", "ndiffports")
o:value("binder", "binder")
if uname.release:sub(1,4) ~= "4.14" then
	o:value("netlink", translate("Netlink"))
end
o = s:option(ListValue, "mptcp_scheduler", translate("Arca TCP scheduler"))
o:value("default", translate("default"))
o:value("roundrobin", "round-robin")
o:value("redundant", "redundant")
if uname.release:sub(1,4) ~= "4.14" then
	o:value("blest", "BLEST")
	o:value("ecf", "ECF")
end
o = s:option(Value, "mptcp_syn_retries", translate("ArcaTCP SYN retries"))
o.datatype = "uinteger"
o.rmempty = false
o = s:option(ListValue, "congestion", translate("Congestion Control"),translate("Default is cubic"))
local availablecong = sys.exec("sysctl -n net.ipv4.tcp_available_congestion_control | xargs -n1 | sort | xargs")
for cong in string.gmatch(availablecong, "[^%s]+") do
	o:value(cong, translate(cong))
end

o = s:option(Value, "mptcp_fullmesh_num_subflows", translate("Fullmesh subflows"))
o.datatype = "uinteger"
o.rmempty = false
o.default = 1
--o:depends("mptcp_path_manager","fullmesh")

o = s:option(ListValue, "mptcp_fullmesh_create_on_err", translate("Re-create fullmesh subflows after a timeout"))
o:value(1, translate("enable"))
o:value(0, translate("disable"))
--o:depends("mptcp_path_manager","fullmesh")

o = s:option(Value, "mptcp_ndiffports_num_subflows", translate("ndiffports subflows number"))
o.datatype = "uinteger"
o.rmempty = false
o.default = 1
--o:depends("mptcp_path_manager","ndiffports")

o = s:option(ListValue, "mptcp_rr_cwnd_limited", translate("Congestion window subflows"))
o:value("Y", translate("enable"))
o:value("N", translate("disable"))
o.default = "Y"
--o:depends("mptcp_scheduler","roundrobin")

o = s:option(Value, "mptcp_rr_num_segments", translate("Consecutiive sgmt sent for round robin"))
o.datatype = "uinteger"
o.rmempty = false
o.default = 1
--o:depends("mptcp_scheduler","roundrobin")

s = m:section(TypedSection, "interface", translate("Interfaces Settings"))
o = s:option(ListValue, "multipath", translate("Arca TCP"), translate("One interface must be set as master"))
o:value("on", translate("enabled"))
o:value("off", translate("disabled"))
o:value("master", translate("master"))
o:value("backup", translate("backup"))
--o:value("handover", translate("handover"))
o.default = "off"


return m
