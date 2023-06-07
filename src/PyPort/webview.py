from mother_board.handling_hw import *
from lib.EZHost import *

def put_hw(src):
    with open("./temp/debug", 'rb') as f:
        return src.replace(b'$logs$', f.read().replace(b'\n', b'<br/>')).replace(b'$values$', b'<tr>' + b'</tr><tr>'.join([b"<td>" + b'</td><td>'.join([item["name"].encode("utf-8"), str(int(item["status"])).encode("utf-8"), str(item.get("comp")).encode("utf-8"), item.get("message").encode("utf-8") if "message" in item else b'Unknow']) + b"</td>" for item in POWERED_COMPONENT]) + b'</td></tr>').replace(b'$keys$', b"<th>Name</th><th>Status</th><th>ID</th><th>Response</th>")

def web_view(address, string_list, connection):

    method = string_list[0]

    if len(string_list) < 2:
        print(f'No file request, address: {address[0]}:{address[1]}, mehod: {method}')
        return

    requesting_file = string_list[1]

    print(f'Client request {requesting_file}, address: {address[0]}:{address[1]}, mehod: {method}')

    path = "./assets/site"
    myfile = requesting_file.split('?')[0]
    myfile = myfile.lstrip('/')

    if(myfile == ''):
        myfile = f'viewer.html'

    try:
        print(path + '/' + myfile)
        file = open(path + '/' + myfile,'rb')
        response = file.read()

        header = 'HTTP/1.1 200 OK\n'

        if(myfile.endswith(".jpg")):
            mimetype = 'image/jpg'
        elif(myfile.endswith(".css")):
            mimetype = 'text/css'
        elif(myfile.endswith(".js")):
            mimetype = "text/javascript"
        elif(myfile.endswith(".ttf")):
            mimetype = "font/ttf"
        else:
            mimetype = 'text/html'

        header += 'Content-Type: '+str(mimetype)+'\n\n'
        file.close()

    except Exception as e:
        header = 'HTTP/1.1 404 Not Found\n\n'
        response = '<html><body><center><h3>Error 404: File not found</h3><p>Python HTTP Server</p></center></body></html>'.encode('utf-8')

    final_response = header.encode('utf-8')
    final_response += response
    if myfile == "viewer.html":
        final_response = put_hw(final_response)
    connection.send(final_response)
    connection.close()

def main() -> int:
    get_connected_hardware()
    M = MyServer()
    M.launch_loop(web_view)
    return (0)

if __name__ == "__main__":
    exit(main())