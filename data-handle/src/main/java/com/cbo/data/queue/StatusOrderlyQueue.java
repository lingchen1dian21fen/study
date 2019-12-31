package com.cbo.data.queue;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.io.Serializable;

/**
 * 有序状态队列
 * @author cbo
 *
 */
public class StatusOrderlyQueue implements Serializable{
	
	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	
	private Node first;
	private Node last;
	
	private int size = 0;
		
	private long minVal = 0;	
	private long interval = 1;
	
	private long timeout = 0;
	
	public StatusOrderlyQueue(long minVal, long interval, long timeout) {
		super();
		this.minVal = minVal;
		this.interval = interval;
		this.timeout = timeout;
	}

	public StatusOrderlyQueue() {
		super();
	}

	/**
	 * 添加
	 * @param e
	 * @return
	 */
	@Deprecated
	public boolean add(Long e){
		final Node newNode = new Node(e);
		if(isEmpty()){
			first = newNode;
			last = newNode;
			size++;
			return true;
		}
		if(newNode.val < first.val){
			newNode.next = first;
			first.prev = newNode;
			first = newNode;
			size ++ ;
			return true;
		}
		if(newNode.val > last.val){
			last.next = newNode;
			newNode.prev = last;
			last = newNode;
			size ++ ;
			return true;
		}
		Node temp = first;
		while(temp != null){
			if(temp.val == newNode.val){
				return false;
			}
			if( newNode.val > temp.val ){
				Node next = temp.next;
				temp = next;
			}else{
				Node prev = temp.prev;
				prev.next = newNode;
				newNode.prev = prev;
				newNode.next = temp;
				temp.prev = newNode;
				size ++;
				return true;
			}
		}
		return false;
	}
	
	/**
	 * 自动增长，优先补充缺省最小值
	 * @return
	 */
	public synchronized Long grow(){
		if(isEmpty()){
			Node newNode = new Node(minVal + interval );
			first = newNode;
			last = newNode;
			size++;
			return minVal + interval;
		}
		if(first.val - minVal > interval){
			Node newNode = new Node(minVal + interval );
			newNode.next = first;
			first.prev = newNode;
			first = newNode;
			size++;
			return minVal + interval;
		}
		Node temp = first;
		while(temp != null){
			Node next = temp.next;
			//tempΪlast�ڵ�
			if(next == null){
				long val = temp.val + interval;
				Node newNode = new Node(val);
				temp.next = newNode;
				newNode.prev = temp;
				last = newNode;
				size ++ ;
				return val;
			}
			if(next.val - temp.val > interval){
				long val = temp.val + interval;
				Node newNode = new Node(val);
				temp.next = newNode;
				next.prev = newNode;
				newNode.prev = temp;
				newNode.next = next;
				size ++;
				return val;
			}else{
				temp = temp.next;
			}
		}
		return null;
	}
	
	/**
	 * 设置状态为完成
	 * @param e
	 * @return
	 */
	public boolean accomplish(Long e){
		Node temp = first;
		while(temp != null){
			if(e == temp.val){
				temp.accomplish = true;
				return true;
			}else{
				temp = temp.next;
			}
		}
		return false;
	}
	
	/**
	 * 清除已完成节点
	 * @return
	 */
	public Long clearAccomplish(){
		while(first != null){
			if(!first.accomplish){
				break;
			}
			Node next = first.next;
			if(next == null){
				break;
			}
			if(next.val - first.val <= interval){
				minVal = first.val;
				first.clear();
				next.prev = null;
				first = next;
				size --;
			}else{
				break;
			}
		}		
		return minVal;
	}
	
	/**
	 * 清除超时节点
	 */
	public void clearTimeout(){
		if(timeout <= 0 || isEmpty()){
			//�޳�ʱ
			return ;
		}
		Node temp = first;
		while( temp != null){
			if( temp.accomplish || System.currentTimeMillis() - temp.ctime <= timeout ){
				temp = temp.next;
			}else{
				Node prev = temp.prev;
				Node next = temp.next;
				if(prev == null && next == null){
					first = null;
					last = null;
				}else if(prev == null && next != null){
					next.prev = null;
					first = next;
				}else if(prev != null && next == null){
					prev.next = null;
					last = prev;
				}else{
					prev.next = next;
					next.prev = prev;
				}
				temp.clear();
				size --;
			}
		}
	}
	
	/**
	 *
	 * @return
	 */
	public Long poll(){
		if(isEmpty()){
			return null;
		}
		Long val = last.val;
		Node prev = last.prev;
		if(prev == null){
			first = null;
			last = null;
		}else{
			prev.next = null;
			last = prev;
		}
		size --;
		return val;
	}
	
	public int size(){
		return size;
	}
	
	
	public boolean isEmpty() {
		return size == 0?true:false;
	}


	/**
	 * @author cbo
	 *
	 */
	private static class Node implements Serializable{
		
		/**
		 * 
		 */
		private static final long serialVersionUID = 1L;
		Long val;
		Node prev;
		Node next;
		long ctime;
		boolean accomplish = false;
				
		public Node(Long val) {
			super();
			this.val = val;
			this.ctime = System.currentTimeMillis();
		}
		
		public void clear(){
			this.val = null;
			this.prev = null;
			this.next = null;
			this.ctime = 0;
			this.accomplish = false;
		}
	}

	/**
	 * 序列化
	 * @return
	 * @throws IOException
	 */
	public byte[] serialize() throws IOException{
		ObjectOutputStream objectOut = null;
		ByteArrayOutputStream out = null;
		out = new ByteArrayOutputStream();
		objectOut = new ObjectOutputStream(out);
		objectOut.writeObject(this);
		byte[] bytes = out.toByteArray();
		if(objectOut != null){
			try {
				objectOut.close();
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
		if(out != null){
			try {
				out.close();
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
		return bytes;
	}
	
	/**
	 * 反序列化
	 * @param bytes
	 * @return
	 * @throws IOException
	 * @throws ClassNotFoundException
	 */
	public static StatusOrderlyQueue deserialize(byte[] bytes) throws IOException, ClassNotFoundException{
		ByteArrayInputStream in = null;
		ObjectInputStream objIn = null;
		in = new ByteArrayInputStream(bytes);
		objIn = new ObjectInputStream(in);
		StatusOrderlyQueue obj = (StatusOrderlyQueue) objIn.readObject();
		if(objIn != null){
			try {
				objIn.close();
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
		if(in != null){
			try {
				in.close();
			} catch (IOException e) {
				e.printStackTrace();
			}
		}
		return obj;
	}
	

}
